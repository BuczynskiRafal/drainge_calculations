import pytest
import calculations as clc


class TestValidateFilling:
    """Set of tests for validate filling method in calculations module.
    # The first test function is named `test_validate_filling_invalid_data_type`.
    The name of the function is a combination of the name of the method
    being tested, the name of the test, and the expected outcome
    """

    def test_validate_filling_invalid_data_type(self):
        """
        This function tests the validate_filling
        function in the clc module to ensure that it raises a TypeError
        when the h and d arguments are not of type float
        """
        with pytest.raises(TypeError):
            clc.validate_filling(h="10", d=20)
            clc.validate_filling(h="10", d="20")
            clc.validate_filling(h=10, d="20")
            clc.validate_filling(h=True, d="20")
            clc.validate_filling(h=10, d=True)
            clc.validate_filling(h=[10], d=20)
            clc.validate_filling(h=10, d=[20])
            clc.validate_filling(h=10, d=None)
            clc.validate_filling(h=None, d=20)

    def test_validate_filling_h_greater_d(self):
        """
        The function `validate_filling` returns `True` if the height
        of the filling is greater than the diameter of the
        cone, and `False` otherwise
        """
        assert clc.validate_filling(h=15, d=0) is False
        assert clc.validate_filling(h=15, d=12) is False
        assert clc.validate_filling(h=25, d=20) is False
        assert clc.validate_filling(h=25.1, d=25) is False

    def test_validate_filling_h_equal_d(self):
        """
        The function returns True if the value of h is less than or equal to the value of d
        """
        assert clc.validate_filling(h=15, d=15) is True
        assert clc.validate_filling(h=20, d=20) is True
        assert clc.validate_filling(h=200, d=200) is True

    def test_validate_filling_h_lower_d(self):
        """
        `validate_filling` returns `True` if `h` is between `0` and `d` (inclusive), and `False` otherwise
        """
        assert clc.validate_filling(h=0, d=20) is True
        assert clc.validate_filling(h=1, d=20) is True
        assert clc.validate_filling(h=10, d=20) is True
        assert clc.validate_filling(h=15, d=20) is True
        assert clc.validate_filling(h=19, d=20) is True
        assert clc.validate_filling(h=19.99, d=20) is True


class TestCalcF:
    pass
