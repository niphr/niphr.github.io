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

