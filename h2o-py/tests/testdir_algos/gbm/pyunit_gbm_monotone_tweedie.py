import h2o
from h2o.estimators import H2OGradientBoostingEstimator
from tests import pyunit_utils


def gbm_monotone_tweedie_test():
    data = h2o.import_file(path=pyunit_utils.locate("smalldata/gbm_test/autoclaims.csv"))
    data = data.drop(['POLICYNO', 'PLCYDATE', 'CLM_FREQ5', 'CLM_FLAG', 'IN_YY'])
    train, test = data.split_frame([0.8], seed=123)
    response = "CLM_AMT5"

    monotone_constraints = {
        "MVR_PTS": 1,
    }

    gbm_mono = H2OGradientBoostingEstimator(monotone_constraints=monotone_constraints, seed=42, distribution="tweedie")
    gbm_mono.train(y=response, training_frame=train, validation_frame=test)

    print(gbm_mono.varimp(use_pandas=True))
    
    print(gbm_mono)


if __name__ == "__main__":
    pyunit_utils.standalone_test(gbm_monotone_tweedie_test)
else:
    gbm_monotone_tweedie_test()
