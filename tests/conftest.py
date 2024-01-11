import os
import pytest
from slither import Slither
from test_generator.main import FoundryTest
from test_generator.fuzzers.Echidna import Echidna
from test_generator.fuzzers.Medusa import Medusa

class TestGenerator:
    def __init__(self, target, target_path, corpus_dir):
        slither = Slither(target_path)
        echidna = Echidna(target, f"echidna-corpora/{corpus_dir}", slither)
        medusa = Medusa(target, f"medusa-corpora/{corpus_dir}", slither)
        self.echidna_generator = FoundryTest("../src/", target, f"echidna-corpora/{corpus_dir}", "./test/", slither, echidna)
        self.medusa_generator = FoundryTest("../src/", target, f"medusa-corpora/{corpus_dir}", "./test/", slither, medusa)

    def echidna_generate_tests(self):
        self.echidna_generator.create_poc()

    def medusa_generate_tests(self):
        self.medusa_generator.create_poc()

@pytest.fixture(autouse=True)
def change_test_dir(request, monkeypatch):
    # Directory of the test file
    test_dir = request.fspath.dirname

    # Path to the test_data directory
    data_dir = os.path.join(test_dir, 'test_data')

    # Change the current working directory to test_data
    monkeypatch.chdir(data_dir)

@pytest.fixture
def basic_types():
    target = "BasicTypes"
    target_path = "./src/BasicTypes.sol"
    corpus_dir = "corpus-basic"

    return TestGenerator(target, target_path, corpus_dir)

@pytest.fixture
def fixed_size_arrays():
    target = "FixedArrays"
    target_path = "./src/FixedArrays.sol"
    corpus_dir = "corpus-fixed-arr"

    return TestGenerator(target, target_path, corpus_dir)

@pytest.fixture
def dynamic_arrays():
    target = "DynamicArrays"
    target_path = "./src/DynamicArrays.sol"
    corpus_dir = "corpus-dyn-arr"

    return TestGenerator(target, target_path, corpus_dir)

@pytest.fixture
def structs_and_enums():
    target = "TupleTypes"
    target_path = "./src/TupleTypes.sol"
    corpus_dir = "corpus-struct"

    return TestGenerator(target, target_path, corpus_dir)