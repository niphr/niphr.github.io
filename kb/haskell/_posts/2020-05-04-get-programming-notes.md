---
layout: post
title: "Notes from Get Programming With Haskell"
date: 2020-05-04
---

## Lesson 5 - Closures and partial application
* order function arguments from the most to least general (e.g. host before id in url generator)
* closure - partial application of some of the arguments

## Lesson 8 - Writing recursive functions
* timing in GHCi `:set +s`

## Lesson 12 - Creating your own types
* record syntax
* type aliases

## Lesson 14 - Using type classes
* Hackage/Stackage - centralized package library (includes minimum complete definitions)
* Hoogle - search engine over the above
* deriving type classes
* `newtype` - sometimes preferred and more efficient way to create type aliases instead of `data`
  * can only be used for types with one type constructor and one type
  * e.g. `newtype Name = Name (String, String) deriving (Show)`

