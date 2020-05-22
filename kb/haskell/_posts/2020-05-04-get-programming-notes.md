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

## Lesson 17 - Design by composition - semigroups and monoids
* Semigroup typeclass - needs to implement `<>` operator - combination of any two instances of the typeclass into one
  * `<>` implementation must be associative, but Haskell compiler does NOT enforce it
* Monoid typeclass - derived from Semigroup, but it also needs an identity element (`x <> id = x`, e.g. for addition it would be 0, for multiplication 1)
  * Lists are the most common Monoids (empty list `[]` is the identity element)
  * Monoid is not actually derived from Semigroup, because it came first, historically
  * mappend is the same as `<>` (or `++` for lists)
  * "m" in mappend, mempty, mconcat stands for Monoid
* typeclass laws - not enforced by compiler, but consumers rely on them, must be ensured
  * Semigroup
    * `<>` must be associative
  * Monoid
    * `mappend mempty x == x`
    * `mappend x mempty == x`
    * mappend must be associative
    * `mconcat = foldr mappend mempty`

## Lesson 18 - Parameterized types
