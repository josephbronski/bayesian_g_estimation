from bayesian_g_estimator import bayesian_g_estimator, ols_g_estimator, brute_force_g_estimator

print(bayesian_g_estimator([(0.3, 0.8)], -3, 3)[:2])
print(ols_g_estimator([(0.3, 0.8)])[:2])
print(brute_force_g_estimator([(0.3, 0.8)])[:2])