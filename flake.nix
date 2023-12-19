{
  # Flake inputs
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };

  # Flake outputs
  outputs = { self, nixpkgs }:
    let
      # Systems supported
      allSystems = [
        "x86_64-linux" # 64-bit Intel/AMD Linux
        "aarch64-linux" # 64-bit ARM Linux
        "x86_64-darwin" # 64-bit Intel macOS
        "aarch64-darwin" # 64-bit ARM macOS
      ];

      # Helper to provide system-specific attributes
      forAllSystems = f: nixpkgs.lib.genAttrs allSystems (system: f {
        pkgs = import nixpkgs { inherit system; };
      });
    in
    {
      # Development environment output
      devShells = forAllSystems ({ pkgs }: {
        default =
          pkgs.mkShell {
            # The Nix packages provided in the environment
            packages = with pkgs; [
              gh
              # Python plus helper tools
              (python311.withPackages (ps: with ps; [
                rich
              ]))
            ];

            shellHook = ''
              echo "welcome to python" | ${pkgs.lolcat}/bin/lolcat
            '';
          };
      });

      # Build the Python package
      packages = forAllSystems ({ pkgs, ... }: {
        default = pkgs.python3Packages.buildPythonPackage {
          pname = "DevAssistant";
          version = "0.1";
          src = ./.;

          propagatedBuildInputs = with pkgs; [
            python3Packages.rich
          ];

          meta = with pkgs.lib; {
            description = "DevAssistant: A helpful tool";
            license = licenses.mit;
          };
        };
      });
    };
}
