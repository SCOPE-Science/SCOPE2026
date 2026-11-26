# Independent mathematical audit

## correctness

PASS

For the defined stationary occupancy Q_t, f(z)=e^(−αz)/2. A reset in (0,t] makes the terminal state conditionally independent of the initial one. Conditional covariance is therefore e^(−rt) times the covariance of the initial threshold and its free Gaussian evolution. Independent Poisson marking gives the bivariate-Poisson law, and total covariance adds the variance of the conditional mean, θ/8. For the Gaussian calculation, scale lengths by α and set G∼N(0,2u). Conditional on G=g, integration of f(z) times the shifted Laplace tail gives e^g/8 for g≤0 and 1/2−(3/8+g/4)e^(−g) for g≥0. Their normal average gives the claimed second integral, using E[e^(−G);G>0]=F(u)/2 and E[G e^(−G);G>0]=√(u/π)−uF(u). Exponential memorylessness above a threshold gives the first integral (1+F(u))/(4α). Strict decay follows by comparing Gaussian threshold probabilities for starting positions on opposite sides of the threshold; the large-lag expansion gives the stated prefactor. At zero lag the two variances are θ/2 and 3θ/8. Given almost every anchor configuration the stationary conditional path process is ergodic (finite-cylinder mixing and approximation), and Q_t has finite conditional mean. The ergodic theorem yields the anchor sum; its Poisson Laplace functional gives all cumulants and the first-anchor decomposition gives the Dickman identity. Independent nested Gaussian quadrature at D=r=ρ=1 produced conditional covariances 0.22294816322803, 0.038545082450942 and 0.00075536467487785 at u=0.2,1.5,5, agreeing with the formula; the frozen script was inspected, not run. Scope clarification: since the displacement starts stationary, Q₀ need not be zero; the occupancy-balance current since that stationary time origin would instead be Q_t−Q₀. The proof establishes the finding for the explicitly defined occupancy only.

## originality

FAIL

The frozen all-lag covariance and plateau have exact existing coverage in the fixed-rate calculation of the rate-disorder Resultary theorem. Its formulas also furnish a short direct implication for the almost-sure time average, with the Dickman identification supplied by the standard Poisson functional. The other record does not explicitly state that distributional identification, and its later catalogue date does not establish historical priority. No claim of an earlier Dickman statement for this gas is made.

## value

PASS

The all-time kernel gives a quantitative separation of dynamical correlation from static anchor variance. The time-average law interprets the surviving frozen disorder despite a simple Poisson marginal. Those are informative structural and physical statistics, not value assigned to the already known one-time law or to a bare special-function substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
