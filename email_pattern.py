def generate_pattern(first_name='', last_name='', middle_name='', domain=''):
	first_initial = ''
	if len(first_name) > 0:
		first_initial = first_name[0]
	last_initial = ''
	if len(last_name) > 0:
		last_initial = last_name[0]
	middle_initial = ''
	if len(middle_name) > 0:
		middle_initial = middle_name[0]

	patterns = []
	patterns.append(first_name)
	patterns.append(last_name)
	patterns.append(first_name+last_name)
	patterns.append(first_name+'.'+last_name)
	patterns.append(first_initial+last_name)
	patterns.append(first_initial+'.'+last_name)
	patterns.append(first_name+last_initial)
	patterns.append(first_name+'.'+last_initial)
	patterns.append(first_initial+last_initial)
	patterns.append(first_initial+'.'+last_initial)

	patterns.append(last_name+first_name)
	patterns.append(last_name+'.'+first_name)
	patterns.append(last_name+first_initial)
	patterns.append(last_name+'.'+first_initial)
	patterns.append(last_initial+first_name)
	patterns.append(last_initial+'.'+first_name)
	patterns.append(last_initial+first_initial)
	patterns.append(last_initial+'.'+first_initial)

	patterns.append(first_initial+middle_initial+last_name)
	patterns.append(first_initial+middle_initial+'.'+last_name)
	patterns.append(first_name+middle_initial+last_name)
	patterns.append(first_name+'.'+middle_initial+'.'+last_name)
	patterns.append(first_name+middle_name+last_name)
	patterns.append(first_name+'.'+middle_name+'.'+last_name)

	patterns.append(first_name+'-'+last_name)
	patterns.append(first_initial+'-'+last_name)
	patterns.append(first_name+'-'+last_initial)
	patterns.append(first_initial+'-'+last_initial)
	patterns.append(last_name+'-'+first_name)
	patterns.append(last_name+'-'+first_initial)
	patterns.append(last_initial+'-'+first_name)
	patterns.append(last_initial+'-'+first_initial)
	patterns.append(first_initial+middle_initial+'-'+last_name)
	patterns.append(first_name+'-'+middle_initial+'-'+last_name)
	patterns.append(first_name+'-'+middle_name+'-'+last_name)
	
	patterns.append(first_name+'_'+last_name)
	patterns.append(first_initial+'_'+last_name)
	patterns.append(first_name+'_'+last_initial)
	patterns.append(first_initial+'_'+last_initial)
	patterns.append(last_name+'_'+first_name)
	patterns.append(last_name+'_'+first_initial)
	patterns.append(last_initial+'_'+first_name)
	patterns.append(last_initial+'_'+first_initial)
	patterns.append(first_initial+middle_initial+'_'+last_name)
	patterns.append(first_name+'_'+middle_initial+'_'+last_name)
	patterns.append(first_name+'_'+middle_name+'_'+last_name)

	if len(domain) > 0:
		for pattern_index in range(len(patterns)):
			patterns[pattern_index] = patterns[pattern_index]+'@'+domain


	return patterns

pattern = generate_pattern('satya', 'gupta', 'prakash', 'skilld.in')