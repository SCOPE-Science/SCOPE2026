# Scientific review: crossing–simple-chord joint law

## Correctness — PASS

The proof conditions on disjoint prescribed consecutive chords. Each such chord crosses nothing; deletion leaves a uniform matching on the residual cyclic order and preserves all crossings. The count of selected cycle edges is the standard cycle-matching formula. Summing these conditional events proves every coefficient of the joint deletion identity. The finite correlation follows from the first two simple-chord factorial moments and the published exact crossing variance (Flajolet–Noy, Theorem 3). The independent joint limit follows by a uniformly dominated factorial-moment expansion and the known crossing central limit theorem. `verify.py` separately enumerates all matchings through seven chords and checks 494 exact assertions. No finite experiment is used as an infinite argument.

## Originality — PASS, with residual priority risk

The 2000 Flajolet–Noy paper proves marginal crossing moments and Gaussian normality, not the mixed law. Acan (2017) proves joint Poisson laws across different short chord lengths, not between short chords and the crossing total. Young (2020) enumerates short chords in linear matchings but does not cover the circular joint crossing polynomial. Paguyo (arXiv:2104.01134, 2021) proves separate quantitative approximations for the two exact observables; Sections 1–4 were compared with the proposed statements and did not include their mixed factorial moments, exact correlation, or joint independence limit. Targeted literature and mathematical-record searches did not identify an equivalent or stronger covering statement. This is best-knowledge priority, not a guarantee about unindexed older literature.

## Value — PASS

Paguyo's two studied observables share the same random diagram, but separate limit laws do not imply independent joint convergence. The theorem closes that natural dependence gap exactly for every finite order, with the unexpectedly simple sharp correlation \(-\sqrt{5/(n+3)}\). It then explains the asymptotic disappearance of finite negative dependence using a structural deletion identity, rather than assuming independence. The result is a motivated bivariate distribution law, not merely an isolated moment computation.

## Scope and limitations

Only consecutive cyclic chords are crossing-neutral under deletion. Higher-length chord statistics require different arguments; an optimal quantitative bivariate convergence rate is not claimed. The proof imports the established crossing CLT, clearly identified in the references. Independent verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
