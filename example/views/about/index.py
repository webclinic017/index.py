from indexpy.http import HTTPView
from indexpy.test import TestView
from indexpy.openapi import describe


class HTTP(HTTPView):
    @describe(
        200,
        """
        text/plain:
            schema:
                type: string
            example:
                about
        """,
    )
    async def get(self):
        """
        about
        """
        return "about"


class Test(TestView):
    def test_get(self):
        resp = self.client.get()
        assert resp.status_code == 200
        assert resp.text == "about"
