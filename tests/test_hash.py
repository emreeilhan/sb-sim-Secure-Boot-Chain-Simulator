from sbsim.hash import sha256_file

def test_sha256_known_value(tmp_path):
    file = tmp_path / "test.bin"
    file.write_bytes(b"abc")

    assert sha256_file(str(file)) == \
        "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
