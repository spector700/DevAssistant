{ python3Packages, lib, ... }:

python3Packages.buildPythonApplication rec {
  pname = "DevAssistant";
  version = "0.1";
  src = ./.;

  propagatedBuildInputs = [
    python3Packages.rich
  ];

  meta = with lib; {
    description = "DevAssistant: A helpful tool";
    license = licenses.mit;
  };
}
