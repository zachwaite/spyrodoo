from numpy import pi
from odoo import http

from spyre.spyre_controller import SpyreController


class SpyrodooController(http.Controller):
    __spyrodoo_model__ = None  # must be implemented by subclass

    def __init__(self):
        super().__init__()
        self.model = self.__spyrodoo_model__()  # type: ignore
        self.spyre_controller = SpyreController(
            templateVars=self.model.templateVars,
            title=self.model.title,
            inputs=self.model.inputs,
            outputs=self.model.outputs,
            controls=self.model.controls,
            tabs=self.model.tabs,
            spinnerFile=self.model.spinnerFile,
            getJsonDataFunction=self.model.getJsonData,
            getDataFunction=self.model.getData,
            getTableFunction=self.model.getTable,
            getPlotFunction=self.model.getPlot,
            getImageFunction=self.model.getImage,
            getD3Function=self.model.getD3,
            getCustomJSFunction=self.model.getCustomJS,
            getCustomCSSFunction=self.model.getCustomCSS,
            getCustomHeadFunction=self.model.getCustomHead,
            getHTMLFunction=self.model.getHTML,
            getDownloadFunction=self.model.getDownload,
            noOutputFunction=self.model.noOutput,
            storeUploadFunction=self.model.storeUpload,
            prefix=self.model.prefix
        )


    @http.route()
    def index(self, **args):
        return self.spyre_controller._index(**args)

    @http.route()
    def plot(self, **args):
        return self.spyre_controller._plot(**args)

    @http.route()
    def image(self, **args):
        return self.spyre_controller._image(**args)

    @http.route()
    def data(self, **args):
        return self.spyre_controller._image(**args)

    @http.route()
    def table(self, **args):
        return self.spyre_controller._table(**args)

    @http.route()
    def html(self, **args):
        return self.spyre_controller._html(**args)

    @http.route()
    def download(self, **args):
        return self.spyre_controller._download(**args)

    @http.route()
    def upload(self, xfile):
        return self.spyre_controller._upload(xfile)

    @http.route()
    def no_output(self, **args):
        return self.spyre_controller._no_output(**args)

    @http.route()
    def spinning_wheel(self, **args):
        return self.spyre_controller._spinning_wheel(**args)

