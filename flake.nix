{
  description = "Archipelago Divinity OS2 development shell";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      systems = [
        "x86_64-linux"
        "aarch64-linux"
      ];

      forEachSystem = f:
        builtins.listToAttrs (map (system: {
          name = system;
          value = f system;
        }) systems);
    in
    {
      devShells = forEachSystem (system:
        let
          pkgs = import nixpkgs {
            inherit system;
          };

          python = pkgs.python313.withPackages (ps: with ps; [
            pip
            setuptools
            wheel
            virtualenv
            cython
            pytest
            pytest-xdist
          ]);
        in
        {
          default = pkgs.mkShell {
            packages = [
              python
              pkgs.git
              pkgs.gcc
            ];

            shellHook = ''
              export PYTHONNOUSERSITE=1

              echo "If you want an isolated environment, run: python -m venv .venv"
              echo "Then activate it with: source .venv/bin/activate"
              echo "Install project deps with: python -m pip install -r requirements.txt -r ci-requirements.txt"
            '';
          };
        });
    };
}