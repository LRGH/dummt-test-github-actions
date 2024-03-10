def test_codeql_1(filename):
    try:
        of = open(filename, "rb")
        try:
            p = pickle.load(of)
        finally:
            of.close()
    except Exception:
        log.info("Pickled training data could not be loaded")

def test_codeql_2(filename):
    try:
        of = open(filename, "rb")
    except Exception:
        of = None
        log.info("Pickled training data could not be opened")
    if of is not None:
        try:
            p = pickle.load(of)
        except Exception:
            log.info("Pickled training data could not be loaded")
        finally:
            of.close()

