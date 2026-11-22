# Self-review

## Correctness — PASS

The exact covariance Gram matrix and integrated covariance sections yield the rational objective in RESULT.md. The strictly positive split derivative on the diagonal proves noncollocation for all positive finite noise; the exact terminal derivative excludes the free endpoint, and a conditional-variance argument excludes the start. Uniform small-inverse-noise expansions, localization at the unique maximizer of the leading function, and a uniform negative Hessian near that point establish high-noise global uniqueness and the two sharp location offsets. The optimized collocation benchmark is separately maximized, and its cubic asymptotic risk differs by exactly \(1/18\). The standalone symbolic checker independently replayed the algebraic identities and the five numerical illustrations. No finite test is used as an infinite proof.

## Originality — PASS with bibliographic qualification

The relevant inspected framework is Ji and Müller (2016), whose fixed-design posterior variance expression is general but does not state the specific all-noise noncollocation and high-noise Brownian optimizer laws. Mukherjee's open paper on processes without quadratic mean derivatives deals with *noiseless* observations and asymptotics in observation count; it explicitly describes the 2003 product-covariance work in the same interpolatory observation setting. The older Müller-Gronbach approach also concerns direct process observations, not two independently noisy sensors. Exact statement-and-implication searches found no broader published result establishing these two-site constants or their optimized replication gap. Residual priority risk is material because the full 2003 article and dissertation were inaccessible. Search absence is not treated as a novelty proof.

## Value — PASS

The problem is a natural constrained short-budget nonlinear placement benchmark. The global fact that no finite amount of independent observation noise makes exact replication optimal is stronger than an optimizer computed at a few noise levels. The explicit high-noise boundary layer gives two different offsets from the free terminal point, a rate of site collision, and a sharp positive third-order cost of forced replication. These are useful for verifying noise-aware numerical design algorithms and for distinguishing path recovery from integration or endpoint estimation; the fact does not follow just by renaming the Brownian-bridge design.

## Remaining limitations

The uniqueness constant is existential, and all-noise uniqueness is not claimed. Older historical work not available in full remains a source-priority uncertainty. No independent validation or peer review is claimed.

Self-review: passed. Independent audit: not yet performed.
