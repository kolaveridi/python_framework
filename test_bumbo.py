import pytest

from api import API


@pytest.fixture
def api():
    return API()

def test_basic_route_adding(api):
    @api.route("/home")
    def home(req, resp):
        resp.text = "Testpytest test_bumbo.py"
    
    with pytest.raises(AssertionError):
        @api.route("/home")
        def home2(req, resp):
            resp.text = "Test2"    