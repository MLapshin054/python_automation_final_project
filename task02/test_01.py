from checkers import checkout
import logging
import yaml

with open("./data.yaml") as f:
    data = yaml.safe_load(f)

def test_step01():
    logging.info("Site check started...")
    assert checkout(f"cd ~; nikto -h {data['test_url']} -ssl -Tuning 4", "0 error(s)"), "Test 1 FAIL"
    logging.info("Checking complete")
