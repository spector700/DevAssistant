{ self }:
{ pkgs, lib, config, ... }:
with lib;

let
  cfg = config.programs.dev-assistant;
in
{
  options.programs.dev-assistant = {
    enable = mkOption {
      type = types.bool;
      default = false;
    };
  };

  config = lib.mkIf cfg.enable {
    home.packages = [ self.packages.${pkgs.stdenv.hostPlatform.system}.default ];
  };
}
