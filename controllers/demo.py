import numpy as np
import pandas as pd
from numpy import pi
from odoo import http
from odoo.addons.spyrodoo.controllers.main import SpyrodooController
from spyre.spyre_model import SpyreModel


class DemoModel(SpyreModel):
    title = "Demo app with random data"
    prefix = "/demo"

    inputs = [
        {
            "type": 'slider',
            "label": 'frequency',
            "key": 'freq',
            "value": 2, "min": 1, "max": 10,
            "action_id": "refresh"
        }, {
            "type": 'multiple',
            "label": 'multiple',
            "options": [
                {"label": "a", "value": "A", "checked": True},
                {"label": "b", "value": "B"},
                {"label": "e", "value": "E", "checked": True},
                {"label": "f", "value": "F"},
                {"label": "g", "value": "G", "checked": True},
                {"label": "h", "value": "H"},
                {"label": "i", "value": "I"},
                {"label": "j", "value": "J"},
                {"label": "k", "value": "K"},
                {"label": "l", "value": "L"},
                {"label": "m", "value": "M"},
                {"label": "n", "value": "N"},
                {"label": "odfeweioufjkjoifdjiojoijfdsiojdfsfdsfefwfefsefwfwewfe", "value": "xoxo"},
                {"label": "c", "value": "C"}
            ],
            "key": 'multi',
            "action_id": "refresh"
        }
    ]

    controls = [{"type": "button", "id": "refresh", "label": "refresh"}]

    outputs = [
        {"type": "html", "id": "htmlx", "control_id": "refresh"},
        {"type": "plot", "id": "plot1", "control_id": "refresh"},
        {"type": "table", "id": "table1", "control_id": "refresh"}
    ]

    def getData(self, params):
        f = float(params['freq'])
        x = np.arange(0, 6 * pi, pi / 50)
        y1 = np.cos(f * x)
        y2 = np.sin(f * x)
        df = pd.DataFrame({"cos": y1, "sin": y2}, index=x)
        df.index.name = "t"
        return df

    def getHTML(self, params):
        return "<h1>This is a heading</h1>"

# TODO: factor this part out
class DemoAppController(SpyrodooController):
    __spyrodoo_model__ = DemoModel

    @http.route("/demo", type="http", auth="user")
    def index(self, **args):
        return super().index(**args)

    @http.route("/demo/plot", type="http")
    def plot(self, **args):
        return super().plot(**args)

    @http.route("/demo/image", type="http")
    def image(self, **args):
        return super().image(**args)

    @http.route("/demo/data", type="http")
    def data(self, **args):
        return super().data(**args)

    @http.route("/demo/table", type="http")
    def table(self, **args):
        return super().table(**args)

    @http.route("/demo/html", type="http")
    def html(self, **args):
        return super().html(**args)

    @http.route("/demo/download", type="http")
    def download(self, **args):
        return super().download(**args)

    @http.route("/demo/upload", type="http")
    def upload(self, xfile):
        return super().upload(xfile)

    @http.route("/demo/no_output", type="http")
    def no_output(self, **args):
        return super().no_output(**args)

    @http.route("/demo/spinning_wheel", type="http")
    def spinning_wheel(self, **args):
        return super().spinning_wheel(**args)

