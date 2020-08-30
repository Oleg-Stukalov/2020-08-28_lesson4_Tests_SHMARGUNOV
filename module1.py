import pytest
from main import multiplication_int, multiplication_string, get_name_hero_by_id


class TestSomething:
    def setup(self):
        print("method setup")
    def teardown(self):
        print("method teardown")
    def test_numbers_3_4(self):
        assert multiplication_int(3, 4) == 12
    @pytest.mark.parametrize("first, second, result", [(3, 4, 12), (5, 0, 0), (-5, 10, -50)])
    def test_numbers(self, first, second, result):
        assert multiplication_int(first, second) == result
    def test_strings_a_3(self):
        assert multiplication_string('a', 3) == 'aaa'
    @pytest.mark.parametrize("id_, expected_result", [(70, 'Batman'), (644, 'Superman'), ('asd', None), ('', None)])
    def test_check_name_hero(self, id_, expected_result):
        assert get_name_hero_by_id(id_) == expected_result