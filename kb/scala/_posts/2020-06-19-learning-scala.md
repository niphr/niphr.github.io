---
layout: post
title: "Notes from learning Scala"
date: 2020-06-19
---

## List of resources
* Programming in Scala, Third Edition
* Functional Programming in Scala

## Introduction
* `val` vs. `var`
* type inference
* primitive Java types are used where possible for performance
* arguments are passed in `args` array
* ! scala 2.13.2 not working with urxvt - bug in JLine? should be fixed, but not in current version, using xfce4-term for now
* recommended indentation style: two spaces
* `i++` and `++i` are not valid, must increment with `i += 1`
* `f(arg)` gets transformed into `f.apply(arg)` - e.g. accessing array value is a method call to `apply`
  * all operations in Scala are method calls
  * assignment = `update` method call (`array(0) = "string" == array.update(0, "string")`)
* array initialization `val x = Array("one", "two")`
* List: `val x = List(1, 2)`
  * cons `::`, concatenation `:::`
* Array is mutable, List is immutable
* if a method name ends with colon (e.g. `::`), it is invoked on the right operand, otherwise on the left one
  * `1 :: x == x.::(1)`
* empty List = `Nil` or `List()`
* useful List methods: `drop, dropRight, count, exists, filter, forAll, length, isEmpty, mkString, reverse, sort`
* tuples 
  * accessing elements through `._1, ._2,...`
* sets
  * there are both mutable and immutable (default) variants
* maps
  * mutable and immutable variants as well

## Classes and Objects
* class members (fields and methods) are public by default
* `procedure` = method called only for it´s side-effect
* classes can´t have static members - Scala has singleton objects instead
  * keyword `object`
  * if `class` and `object` have the same name, the object is called the `companion object`
    * companion class and object have to be defined in the same file
  * singleton objects can´t be parameterized, unlike classes (s. objects can´t be instantiated with a `new` keyword)
* `standalone object` - when the object´s name does not match a class name (useful for e.g. encapsulating related methods)
* application entry point
  * any standalone singleton object with a proper signature (type Unit, args parameter)
* App trait - eliminates need to define main method, automatically exposes args

## Basic Types and Operations
* string interpolators: `s`, `raw`, `f`
* all methods can be used in operator notation (e.g. `"hello" contains "o"` or `7 toLong`)
* only `+, -, !, ~` can be used as prefix operators
* convention on using parentheses when invoking methods: if method has side effects, include them (`println()`), otherwise they are not needed (`"Hello".toLowerCase`)
* logical operators: `||, &&` - short-circuit (from left; right side may not be evaluated)
  * non-short-circuiting variants: `|, &`
* bitwise operations: or `|`, and `&`, xor `^`, complement `~`
  * shift left `<<`, shift right `>>`, unsigned shift right `>>>`
