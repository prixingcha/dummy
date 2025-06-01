from common_modules.all_in_one_module import print,os,sys,LLMSelector, ModelConfigurator, model_choices
import pdb


return_val = LLMSelector(model_choices).run()
configurator = ModelConfigurator(return_val).configure()

#pdb.set_trace()

# selector = LLMSelector(model_choices)
# return_val = selector.run()
# configurator = ModelConfigurator(return_val)
# configurator.configure()
