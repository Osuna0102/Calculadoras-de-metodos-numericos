from pybigparser import evaluator

mybig = evaluator.bigFunction()
mybig.setFunction("x**2+2*y")
mybig.addSub("x", "24+6*c")
mybig.addSub("y", "25 / d")
mybig.addSub("c", "1")
mybig.addSub("d", "4")

mybig.evaluate()

mybig.getSubValue("x")
mybig.getSubValue("y")
