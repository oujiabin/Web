import os
import time
import logging


def init_env(base_dir, report_name):
    """
    Generate test directory
    """

    if os.path.isdir(base_dir) is False:
        os.mkdir(base_dir)

    report_path = os.path.join(base_dir, report_name)
    report_snapshot = os.path.join(base_dir, report_name, "snapshot")

    os.mkdir(report_path)
    os.mkdir(report_snapshot)
    logging.info("测试报告目录创建完成!")


def web_report_dir(base_dir):
    """
    Get the web test reports directory
    :param base_dir:
    :return:
    """
    now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
    report_name = "Allure_" + now_time
    init_env(base_dir, report_name)
    return os.path.join(base_dir, report_name), report_name
