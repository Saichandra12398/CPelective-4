import os,sys
sys.path.append(os.getcwd())
from nth_kaprekarnumber import fun_nth_kaprekarnumber
import pytest


@pytest.mark.parametrize('a, result',[
    (0,1),(1,9),(5,297),
(10,4950),(15,17344),(20,99999)
])
def test_fun_nth_kaprekarnumber(a, result):
    assert fun_nth_kaprekarnumber(a) == result

