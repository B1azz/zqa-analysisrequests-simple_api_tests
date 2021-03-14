import json

analysis_request = {}
all_sample_analysis_request = []
sample_analysis_request0 = {}
sample_analysis_request1 = {}
all_sample_job_orders0 = []
all_sample_job_orders1 = []
sample_job_order00 = {}
sample_job_order01 = {}
sample_job_order10 = {}
sample_job_order11 = {}


def get_analysis_request():
    print(analysis_request)
    return analysis_request


def get_all_sample_analysis_request():
    return all_sample_analysis_request


def get_sample_analysis_request0():
    return sample_analysis_request0


def get_sample_analysis_request1():
    return sample_analysis_request1


def get_all_sample_job_orders0():
    return all_sample_job_orders0


def get_all_sample_job_orders1():
    return all_sample_job_orders1


def get_sample_job_order00():
    return sample_job_order00


def get_sample_job_order01():
    return sample_job_order01


def get_sample_job_order10():
    return sample_job_order10


def get_sample_job_order11():
    return sample_job_order11


class CreateJson:
    # region analysis_request

    def add_analysis_request_id(self, analysis_request_id):
        new = {"id": analysis_request_id}
        analysis_request.update(new)

    def add_analysis_request_code(self, analysis_request_code):
        new = {"code": analysis_request_code}
        analysis_request.update(new)

    def add_analysis_request_sample_template(self, analysis_request_sample_template):
        new = {"sampleTemplate": analysis_request_sample_template}
        analysis_request.update(new)

    def add_analysis_request_material(self, analysis_request_material):
        new = {"material": analysis_request_material}
        analysis_request.update(new)

    def add_analysis_request_material_lot(self, analysis_request_material_lot):
        new = {"materialLot": analysis_request_material_lot}
        analysis_request.update(new)

    def add_analysis_request_start_time(self, analysis_request_start_time):
        new = {"startTime": analysis_request_start_time}
        analysis_request.update(new)

    def add_analysis_request_end_time(self, analysis_request_end_time):
        new = {"endTime": analysis_request_end_time}
        analysis_request.update(new)

    def add_analysis_request_description(self, analysis_request_description):
        new = {"description": analysis_request_description}
        analysis_request.update(new)

    def add_analysis_request_source_type(self, analysis_request_source_type):
        new = {"sourceType": analysis_request_source_type}
        analysis_request.update(new)

    def add_analysis_request_source(self, analysis_request_source):
        new = {"source": analysis_request_source}
        analysis_request.update(new)

    def add_analysis_request_subdivision(self, analysis_request_subdivision):
        new = {"subdivision": analysis_request_subdivision}
        analysis_request.update(new)

    def add_all_sample_analysis_request(self, sample_analysis_request):
        new = {"sampleAnalysisRequests": sample_analysis_request}
        analysis_request.update(new)

    def add_sample_analysis_request(self, sample_analysis_request):
        all_sample_analysis_request.append(sample_analysis_request)

    # endregion

    # region sample_analysis_request
    def add_sample_id(self, sample_id, sample=0):
        new = {"id": sample_id}
        if sample == 0:
            sample_analysis_request0.update(new)
        if sample == 1:
            sample_analysis_request1.update(new)

    def add_sample_code(self, sample_code, sample=0):
        new = {"code": sample_code}
        if sample == 0:
            sample_analysis_request0.update(new)
        if sample == 1:
            sample_analysis_request1.update(new)

    def add_sample_num(self, sample_num, sample=0):
        new = {"num": sample_num}
        if sample == 0:
            sample_analysis_request0.update(new)
        if sample == 1:
            sample_analysis_request1.update(new)

    def add_sample_order(self, sample_order, sample=0):
        new = {"order": sample_order}
        if sample == 0:
            sample_analysis_request0.update(new)
        if sample == 1:
            sample_analysis_request1.update(new)

    def add_sample_sampling_point(self, sample_sampling_point, sample=0):
        new = {"samplingPoint": sample_sampling_point}
        if sample == 0:
            sample_analysis_request0.update(new)
        if sample == 1:
            sample_analysis_request1.update(new)

    def add_sample_sampling_date(self, sample_sampling_date, sample=0):
        new = {"samplingDate": sample_sampling_date}
        if sample == 0:
            sample_analysis_request0.update(new)
        if sample == 1:
            sample_analysis_request1.update(new)

    def add_sample_sample_log(self, sample_sample_log, sample=0):
        new = {"sampleLog": sample_sample_log}
        if sample == 0:
            sample_analysis_request0.update(new)
        if sample == 1:
            sample_analysis_request1.update(new)

    def add_sample_description(self, sample_description, sample=0):
        new = {"description": sample_description}
        if sample == 0:
            sample_analysis_request0.update(new)
        if sample == 1:
            sample_analysis_request1.update(new)

    def add_sample_quantity(self, sample_quantity, sample=0):
        new = {"quantity": sample_quantity}
        if sample == 0:
            sample_analysis_request0.update(new)
        if sample == 1:
            sample_analysis_request1.update(new)

    def add_sample_quantity_uom(self, sample_quantity_uom, sample=0):
        new = {"quantityUom": sample_quantity_uom}
        if sample == 0:
            sample_analysis_request0.update(new)
        if sample == 1:
            sample_analysis_request1.update(new)

    def add_all_sample_job_orders(self, sample_job_orders, sample=0):
        new = {"sampleJobOrders": sample_job_orders}
        if sample == 0:
            sample_analysis_request0.update(new)
        if sample == 1:
            sample_analysis_request1.update(new)

    def add_sample_job_order(self, sample_job_order, sample=0):
        if sample == 0:
            all_sample_job_orders0.append(sample_job_order)
        if sample == 1:
            all_sample_job_orders1.append(sample_job_order)

    TODO: 'Второй sampleJobOrders'

    # endregion


if __name__ == '__main__':
    j = CreateJson()
    j.add_analysis_request_id('1234')
    j.add_sample_id('123')
    j.add_sample_id('122', sample=1)

    j.add_sample_job_order(get_sample_job_order00(), sample=0)
    j.add_sample_job_order(get_sample_job_order01(), sample=0)
    j.add_all_sample_job_orders(get_all_sample_job_orders0())

    j.add_sample_job_order(get_sample_job_order10(), sample=1)
    j.add_sample_job_order(get_sample_job_order11(), sample=1)
    j.add_all_sample_job_orders(get_all_sample_job_orders1())

    j.add_sample_analysis_request(get_sample_analysis_request0())
    j.add_sample_analysis_request(get_sample_analysis_request1())
    j.add_all_sample_analysis_request(get_all_sample_analysis_request())
    get_analysis_request()
