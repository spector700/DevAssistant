{ pkgs, lib, config, ... }:
with lib;
let
  cfg = config.programs.dev-assistant;
in
{
  options.programs.dev-assistant = {
    enable = lib.mkEnableOption;
  };

  config = lib.mkIf cfg.enable {
    home.packages = [ cfg.package ];
  };
}
