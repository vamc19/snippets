__author__ = 'vamc'

import mechanize
import random

# Change url and values accordingly.
url = "http://surveymonkey.com/s/xxxxxxx"

# Question 1
q1 = "input_632699792_10_0_0"           # values [7324424142_0, 7324424143_0]
# Options for Q1.
q1_values = ["7324424142_0", "7324424143_0"]

q2 = "input_632717766_10_0_0"           # values [7324659835_0, 7324659836_0, 7324659837_0, 7324659838_0]
q2_values = ["7324659835_0", "7324659836_0", "7324659837_0", "7324659838_0"]

q3 = "input_632718086_10_0_0"           # values [7324691661_0, 7324691662_0, 7324691663_0, 7324691664_0]
q3_values = ["7324691661_0", "7324691662_0", "7324691663_0", "7324691664_0"]

q4 = "input_632718148_10_0_0"           # values [7324691933_0, 7324691934_0, 7324691935_0, 7324691936_0]
q4_values = ["7324691933_0", "7324691934_0", "7324691935_0", "7324691936_0"]

q5 = "input_632718369_10_0_0"           # values [7324683411_0, 7324683412_0, 7324683413_0]
q5_values = ["7324683411_0", "7324683412_0", "7324683413_0"]

q6 = "input_632720312_10_0_0"           # values [7324664364_0, 7324664365_0]
q6_values = ["7324664364_0", "7324664365_0"]

for i in xrange(42):
    br = mechanize.Browser()
    br.open(url)
    br.select_form("frmS")
    br.form.set_value([random.choice(q1_values)], name=q1)
    br.form.set_value([random.choice(q2_values)], name=q2)
    br.form.set_value([random.choice(q3_values)], name=q3)
    br.form.set_value([random.choice(q4_values)], name=q4)
    br.form.set_value([random.choice(q5_values)], name=q5)
    br.form.set_value([random.choice(q6_values)], name=q6)
    br.submit()
    resp = br.response().read()
    if "Survey done! Take more surveys by signing up | SurveyMonkey" in resp:
        print "Survey posted successfully"
    else:
        print resp




