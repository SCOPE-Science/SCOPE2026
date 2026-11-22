# Scientific self-review

## Correctness — PASS

The proof conditions on entire stationary source paths and uses the standard immigration–death Poisson representation with independent exponentially distributed lifetimes. The key nonstandard bookkeeping step is to retain the covariance \(K_X(t)=s(3+t)e^{-t}/2\) of the **non-Poisson** intermediate addition output, rather than replacing it by a source Poisson process. In the distributed circuit, combining the two intermediate products into \(P=U+V\) exactly recovers the common-catalyst driver \((A+B)C\). All required integrals are elementary and absolutely convergent. Both means and variances are calculated for all \(a,b,c>0\), and sign classification follows because \((a+b)c>0\). Exact rational tests provide diagnostics, not a proof by enumeration.

## Originality — PASS against inspected evidence

Anderson and Moon (arXiv:2611.11069v1, Sections 3–7) define these modules and display both equivalent-mean mixed-operation architectures, but derive comparative results for repeated addition or repeated multiplication rather than the explicit distributive-law variance boundary. Their Corollary 4.4 is the necessary established queue covariance tool and is fully credited. The uninspected full text of Dean and Ganesh (2022), DOI 10.1007/s00285-022-01781-9, is a priority risk because it treats tandem infinite-server queues; available publisher material does not resolve whether its broad results imply this exact comparison. No claim of exhaustive uniqueness is made.

## Value — PASS

The sharply quantified boundary \(a+b+4c=4/3\) proves that the cheaper independent-stationary-readout architecture changes with source intensities, although the encoded mean is identical. The common multiplier source has four times the threshold weight of either addend. The result targets the mixed-arithmetic fluctuation problem expressly motivated in the primary source, rather than an arbitrary tiny parameter case. It does not settle trajectory-average costs or nonunit kinetics.

## Verification and limits

The analytical proof is in `RESULT.md`. Running `python3 verify.py` from this directory checks the variance formulas, exact symmetry threshold, and both strict regimes with rational arithmetic. The checker only tests finitely many inputs. Earlier queueing full text remains partly inaccessible, and a separate independent mathematical audit has not been undertaken.

Self-review: passed. Independent audit: not yet performed.
