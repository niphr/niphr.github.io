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
* kinds - types of types (`:kind (,,)` to find out kind of triple)
* qualified imports `import qualified Data.Map as Map`
* `Data.Map`
  * `fromList` to build maps
  * `lookup` to get value

## Lesson 21 - Hello world! - Introducing IO types
* `IO` - parameterized type providing context (this code is impure, may change state)
  * `IO` actions are not functions
* values must stay in the context of `IO` - unlike e.g. `Maybe a`, you can´t transform `IO a` to `a`
* `do` notation - different assignment options:
  * `let x = y` - `y` must not be of `IO`-type
  * `x <- getLine` - getLine is `IO` action, but `x` can be later treated as `a`, not `IO a`

## Lesson 22 - Interacting with the command-line and lazy IO
* `getArgs :: IO [String]` to read command-line arguments
* `mapM` - map in the context of a `Monad` (can´t use regular `map`)
* `mapM_` - same as above, but returns no value
* `print` - same as `(putStrLn . show)`
* `replicateM n ioAction` - repeats `ioAction` `n` times
* `getContents` - reads stdin, treating is as a lazy list of characters
* `lines`, `splitOn`

## Lesson 23 - Working with text and Unicode
* `Data.Text` is preferable to `String` (for almost any practical application, althought `String` is instructional in the learning phase)
  * differences: array vs. linked list, better efficiency, strict vs. lazy evaluation, good Unicode support
* language extensions, e.g. OverloadedStrings
* `Data.Text.IO` for working with `IO Text` - no need to convert between `String` and `Text`

## Lesson 24 - Working with files
* functions that work with handles (`hGetContents`, `hGetLine`) vs. files (`readFile`, `appendFile`) - the latter are generally more abstract and easier to use
* lazy evaluation can lead to tricky bugs (closing the handle before the file contents have been evaluated) -> in more complex programs, strict evaluation of file IO is preferred

## Lesson 25 - Working with binary data
* `ByteString`
