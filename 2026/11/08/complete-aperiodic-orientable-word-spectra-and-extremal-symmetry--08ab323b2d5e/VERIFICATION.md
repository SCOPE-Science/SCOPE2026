---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

The exact finite theorem uses only two complete, standalone Python 3 standard-library programs and the supplied complete `ENUMERATION.json` data file.

Run these commands from the extracted-file directory:

```sh
python3 verify_bitmask.py ENUMERATION.json
python3 verify_direct.py ENUMERATION.json
```

The recorded outputs were:

```text
span=6 words=22 orbits=6 length+1=0
span=7 words=3294 orbits=829 length+1=0
VERIFY_BITMASK_OK
span=6 normalized=11 fixed_normalized=1 max+1=0
span=7 normalized=1647 fixed_normalized=11 max+1=0
VERIFY_DIRECT_OK
```

The first program uses canonical integer reversal-orbit IDs and bitsets; the second uses literal strings and sets of visited factors. Both enumerate **every** legal first-bit-zero prefix and each of its admissible bit extensions, without randomization. The second also compares against direct complete enumeration of all binary strings at four smaller input sizes. Both establish that no legal word extends the reported maximum by even one bit; every longer legal word would yield an excluded prefix, so maximality follows.

The data file contains the exact labeled count at every length for spans six and seven, all first-bit-zero maximum-length words, endpoint and Hamming-weight profiles, reverse-complement fixed points and orbit counts. Full labeled lists are exactly their union with bit complements. The explicit coverage induction is in `RESULT.md`.

All assertions are finite. No claim is made about larger spans or nonbinary alphabets, and neither program constitutes an independent external audit. The provenance comparison is not proof that no unknown earlier enumeration exists.
