# Independent mathematical audit

## correctness

PASS

Independently factor K=L diag(I,-S)L^T, with L having lower-left block A and identity diagonal. Then B=L diag(I,Pi)L^{-1}; B is idempotent, with rank n+rank(Pi), so singular precisely for a nontrivial omission. On the image of the zero-start Krylov space every positive order fits only the line through B(b,0), giving t=E/(E+R²) and the stated squared residual. K is invertible, so ker(B)=ker(the inverse application) and the original-variable reconstruction is independent of any nonuniqueness in the transformed iterate. Applying the inverse application to t(b,0) gives x_G=t Pi x_*; Parseval gives the error identity. In an omitted Fourier mode the range line is (1,a_j), giving the stated floor. The two-mode rational witness gives 4/3 versus 4/5 and squared error 1/9+4/25=61/225. Strictness is possible, not universal; for example both floors vanish for R=0. Attenuation affects nonzero retained components when R>0. The result concerns mathematical Krylov minima, not iterates executable after breakdown. Replay: frozen RESULT.md §§Assumptions and scope, Proof and verify_pupil.py lines 6–85; checker inspected, not executed. Its seeded examples do not prove the universal claims.

## originality

FAIL

A distinct indexed record gives the same all-positive-order plateau and attained range floor in a broader complex circulant model. Its exact minimizing scalar and transformed image Bc also force the physical reconstruction and hence its retained-mode bias and error. This is established statement-level coverage; the records' displayed dates do not establish who first obtained it.

## value

FAIL

A well-conditioned witness separating a physical range obstruction from a Krylov obstruction is a useful phenomenon. But that separation and its exact formulas are covered, and the only apparent extra claim (retained reconstruction) is a direct block solve with the already determined fitted vector. The frozen finding supplies no independent exact law beyond that covered mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
