import sys
from logger import logging


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occoured in python script name {file_name} in line {line_number} and error is {error}"

    return error_message


class CustomException(Exception):
    def __init__(self, error_msg, error_detail: sys):
        super().__init__(error_msg)
        self.error_msg = error_message_detail(
            error=error_msg, error_detail=error_detail
        )

    def __str__(self):
        return self.error_msg
