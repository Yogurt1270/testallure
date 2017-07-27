#!/usr/local/bin
# coding:utf-8

import pytest


class Test(object):
    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_function1(self):
        print("testcase1")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_function2(self):
        print("testcase2")
