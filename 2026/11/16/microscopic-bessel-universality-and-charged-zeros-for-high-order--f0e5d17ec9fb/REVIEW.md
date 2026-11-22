# Independent mathematical audit

## correctness

PASS

From the exact true-polyanalytic Fock kernel, K_n(u,v)=exp(i Im(u bar(v))/n - |u-v|^2/(2n)) L_n(|u-v|^2/n). Its Laguerre power-series coefficients equal (-t)^k/(k!)^2 times a_nk=prod_{j<k}(1-j/n) for k<=n, else zero. Bonferroni gives |a_nk-1+k(k-1)/(2n)|<=O(k^4/n^2), uniformly summable against factorial-square weights with arbitrarily many derivatives on fixed t intervals. The Bessel ODE tH''+H'+H=0 converts the O(1/n) Laguerre and Gaussian corrections to tH'/2; the magnetic phase contributes i omega H. Covariance derivative bounds imply finite-dimensional convergence and C^s tightness of proper Gaussian fields on every compact; the circular-average Fourier representation gives the limit Helmholtz equation (Delta+4)W=0. The field value has bounded two-dimensional Gaussian density, so the vector-valued Bulinskaya/transversality argument excludes critical zeros; under C^1 compact convergence simple zeros match and preserve real-Jacobian signs, giving joint vague point-process convergence. For the one-point Kac–Rice law at 0, independent complex Gaussian derivatives yield aE1-bE2 (a=(n+1)/n, b=1), giving rho_(n,±)=(n+1/2+1/(4n+2)±1)/(2pi n). An independent SciPy evaluation checked the two-term Laguerre expansion at t=0,0.5,2.25,5 for n=100,250,600 (12 numerical cases), and the finite coefficients/derivative laws were inspected; this is corroboration, not a proof of field tightness or point-process convergence.

## originality

PASS

Known exact fixed-index polyanalytic Fock covariance and zero-intensity formulas and classical Mehler–Heine/Bessel limits are correctly treated as inputs. The highly relevant 2026 Abreu–Shirai original 48-page paper treats cross-level zero pair correlations and averages across levels, not an individual n->infinity u/√n random-wave field/charged-zero-process convergence in inspected main results; Bellourak et al 2026 study fixed Hermite order charged zeros. The new two-term magnetic correction and complete charged zero-process limit are not directly implied by those statements. Alternative high-Landau-level local-universality prior art remains a named risk.

## value

PASS

The microscopic high-order Hermite spectrogram regime is a natural scaling for time-frequency zero geometry. Identifying a genuinely translation-invariant monochromatic Gaussian random wave, exact leading magnetic finite-order correction, and convergence of both topologically charged zero processes supplies structural statistics beyond classical fixed-order intensity calculations and averaged-energy theorems. The exact charged values act as consistency checks rather than novelty by themselves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
