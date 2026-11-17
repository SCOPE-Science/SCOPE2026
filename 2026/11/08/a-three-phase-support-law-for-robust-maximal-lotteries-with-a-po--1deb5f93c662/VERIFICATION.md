---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS. For the two explicitly given skew matrices and θ interval, minimizing the bilinear margin separately over pure opposing alternatives and interval endpoints yields V_r(p)=min{-ru[(1-z)/2+|d|]+z[w-v-r(w+v)]/2, (v-w)(1-z)/2-r(v+w)|d|}. Since r,u,v,w>0 both terms strictly decrease with |d|, every maximizer has x=y=(1-z)/2. The resulting lower envelope of f1(z)=-ru/2+[w-v+r(u-w-v)]z/2 and f3(z)=(v-w)(1-z)/2 gives the stated complete r=1 support classification including u=2v ties. For w<v,u>2v, f1<0<=f3, so the slope changes sign exactly at rc=(v-w)/(u-v-w) in (0,1), leading to z=0, arbitrary z, then z=1, although C is a strict pooled Condorcet loser. The exhibited twenty-ballot groups have exact margins (4/5,1/5,1/10), rc=1/5; rational LP implementation independently checks 625 finite parameter-grid inputs. All-r theorem is only claimed for this specified reversal region.

## originality

PASS

PASS qualified. Khalaf et al. (2026) introduce robust maximal lotteries for variable population weights, prove robust Condorcet/dominance rules and a general linear programming characterization, all established and acknowledged. The inspected main text/appendix does not give the exact closed-form mirrored-opposed-winner support chambers or a strict pooled Condorcet loser becoming unique under increased uncertainty with a rational sharp radius. A generic finite LP is an algorithm for any instance, not an explicit all-positive-parameter classification, and the earlier fixed-majority maximal lotteries differ from a minimax range over θ. An unindexed application of the same LP could give an equivalent reversal; no absolute priority claimed.

## value

PASS

PASS. The exact symmetric two-constituency case is a motivated boundary test for robust group-weight aggregation: a method intended to protect against population-shift risk can choose a candidate that is a strict Condorcet loser of the pooled electorate. The threshold rc and complete r=1 analytic support table provide interpretable structural, normative information beyond solving sample LPs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
