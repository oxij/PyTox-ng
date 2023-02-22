with import <nixpkgs> {};
with python3Packages;

buildPythonPackage rec {
  pname = "PyTox-ng";
  version = "git";
  disabled = !isPy3k;

  src = lib.cleanSourceWith {
    src = ./.;
    filter = name: type: let baseName = baseNameOf (toString name); in
      lib.cleanSourceFilter name type && ! (
        (baseName == "default.nix") ||
        (baseName == "result") ||
        (builtins.match ".*/results(|/.*)" name != null)
      );
  };

  nativeBuildInputs = [
    sphinx texinfo
  ];

  propagatedBuildInputs = [
    libtoxcore
    libvpx libopus libsodium
  ];

  # tests require networking
  doCheck = false;

  # build and install docs
  postInstall = ''
    export PYTHONPATH=$out/lib/*/site-packages:$PYTHONPATH
    make -C docs html man info
    find .

    install -Dd $out/share/doc/pytox
    cp -r docs/_build/html $out/share/doc/pytox

    install -Dd $out/share/info
    cp -r docs/_build/texinfo/*.info $out/share/info

    install -Dd $out/share/man/man7
    cp -r docs/_build/man/*.7 $out/share/man/man7
  '';
}
