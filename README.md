# WIP

# Python Package for Downloading Solutions

A Python package that aggregates competitive programming solutions from different judges.  

Project configuration is currently done in a config.yml file.  See below for configuration models for various judges/supported sites.

## General Notes

* If you have made multiple AC submissions to a problem, the last AC will be taken
* Files will not be overwritten, so no solution will be downloaded multiple times unless if the solution file is removed
* If multiple accounts are specified for a judge, and they all have AC on some problem, the account listed earlier will have its submissions prioritized

## Command Options

```
autogenerate this...
```

# Available Judges

## DMOJ (and derivatives)

Note that the site URL must be specified.  Additionally, this package uses DMOJ APIv2 for querying submissions.  If the version of DMOJ being run does not support APIv2, this will currently not work.

## Codeforces

Note that only public solutions will be downloaded, so that does not include the `acm.sgu.ru` problems and gyms.

## AtCoder

(Is this even possible?)

## CodeChef

This is possible I think

## Kattis

(Is this even possible?)

## SPOJ

(Is this even possible?)

## oj.uz

(Is this even possible?)

## Baekjoon Online Judge (acmicpc.net)

(Is this even possible?)

## HackerRank

(Is this even possible?)

## TopCoder

(Is this even possible?)
## WCIPEG

WCIPEG submissions have been migrated to DMOJ.  See [here](https://dmoj.ca/post/186-peg-accounts-and-problems-are-now-accessible) on information on how to merge accounts.  See above for downloading submissions on DMOJ.

## Google Code Jam

(Is this even possible?)

## Facebook HackerCup

(Is this even possible?)

