{
  python3Packages,
  pkgs,
  lib,
  ...
}:

python3Packages.buildPythonApplication {
  pname = "DevAssistant";
  version = "0.1";
  src = ./.;

  propagatedBuildInputs = [
    pkgs.gh
    python3Packages.rich
  ];

  meta = with lib; {
    description = "DevAssistant: A helpful tool";
    license = licenses.mit;
  };
}
