#! python

'''
	DESCRIPTION = 'description'
	FORWARD = 'forward'
	BACK = 'back'
	LEFT = 'left'
	RIGHT = 'right'
	GROUND = 'ground'
	INVENTORY = 'inventory'
'''

'''
		DESCRIPTION : ''
		FORWARD : ''
		BACK : ''
		LEFT : ''
		RIGHT: ''
		GROUND: ''
'''

Physical_Rooms = {
	'Prison Cell' : {
		DESCRIPTION : 'desc'
		FORWARD : 'door'
		BACK : 'lamp'
		LEFT : ''
		RIGHT: ''
		GROUND: 'lighter'
	} ,

	'Hallway' : {
		DESCRIPTION : 'desc'
		FORWARD : 'gate'
		BACK : 'Prison Cell'
		LEFT : 'Cells 1 and 2'
		RIGHT: 'Cells 3 and 4'
		GROUND: ''	
	}

	'Cells 1 and 2' : {
		DESCRIPTION : ''
		FORWARD : ''
		BACK : ''
		LEFT : 'Cell 1'
		RIGHT: 'Cell 2'
		GROUND: ''
	}

	'Cells 3 and 4' : {
		DESCRIPTION : ''
		FORWARD : ''
		BACK : ''
		LEFT : 'Cell 3'
		RIGHT: 'Cell 4'
		GROUND: ''
	}
	
	'Cell 1' : {
		DESCRIPTION : ''
		FORWARD : ''
		BACK : ''
		LEFT : ''
		RIGHT: ''
		GROUND: ''
	}

	'Cell 2' : {
		DESCRIPTION : ''
		FORWARD : ''
		BACK : ''
		LEFT : ''
		RIGHT: ''
		GROUND: ''
	}

	'Cell 3' : {
		DESCRIPTION : ''
		FORWARD : ''
		BACK : ''
		LEFT : ''
		RIGHT: ''
		GROUND: ''
	}

	'Cell 4' : {
		DESCRIPTION : ''
		FORWARD : ''
		BACK : ''
		LEFT : ''
		RIGHT: ''
		GROUND: ''
	}

	'Gate' : {
		DESCRIPTION : ''
		FORWARD : ''
		BACK : ''
		LEFT : ''
		RIGHT: ''
		GROUND: ''
	}
}

Introspective_Choices = {
	
	'What' : {

		DESCRIPTION : '',
		LITERAL_RESPONSE : {
			RESPONSE_TEXT : '',
			FOLLOWUP_DESCRIPTION : '',
			FOLLOWUP_LITERAL_RESPONSE : '',
			FOLLOWUP_FRACTAL_RESPONSE : ''
		},

		FRACTAL_RESPONSE : {
			RESPONSE_TEXT : '',
			FOLLOWUP_DESCRIPTION : '',
			FOLLOWUP_LITERAL_RESPONSE : '',
			FOLLOWUP_FRACTAL_RESPONSE : ''
		}
	}

	'Who' : {
		DESCRIPTION : '',
		LITERAL_RESPONSE : {
			RESPONSE_TEXT : '',
			FOLLOWUP_DESCRIPTION : '',
			FOLLOWUP_LITERAL_RESPONSE : '',
			FOLLOWUP_FRACTAL_RESPONSE : ''
		},

		FRACTAL_RESPONSE : {
			RESPONSE_TEXT : '',
			FOLLOWUP_DESCRIPTION : '',
			FOLLOWUP_LITERAL_RESPONSE : '',
			FOLLOWUP_FRACTAL_RESPONSE : ''
		}
	}

	'Where' : {
		DESCRIPTION : '',
		LITERAL_RESPONSE : {
			RESPONSE_TEXT : '',
			FOLLOWUP_DESCRIPTION : '',
			FOLLOWUP_LITERAL_RESPONSE : '',
			FOLLOWUP_FRACTAL_RESPONSE : ''
		},

		FRACTAL_RESPONSE : {
			RESPONSE_TEXT : '',
			FOLLOWUP_DESCRIPTION : '',
			FOLLOWUP_LITERAL_RESPONSE : '',
			FOLLOWUP_FRACTAL_RESPONSE : ''
		}
	}

	'When' : {
		DESCRIPTION : '',
		LITERAL_RESPONSE : {
			RESPONSE_TEXT : '',
			FOLLOWUP_DESCRIPTION : '',
			FOLLOWUP_LITERAL_RESPONSE : '',
			FOLLOWUP_FRACTAL_RESPONSE : ''
		},

		FRACTAL_RESPONSE : {
			RESPONSE_TEXT : '',
			FOLLOWUP_DESCRIPTION : '',
			FOLLOWUP_LITERAL_RESPONSE : '',
			FOLLOWUP_FRACTAL_RESPONSE : ''
		}
	}

	'Why' : {
		DESCRIPTION : '',
		LITERAL_RESPONSE : {
			RESPONSE_TEXT : '',
			FOLLOWUP_DESCRIPTION : '',
			FOLLOWUP_LITERAL_RESPONSE : '',
			FOLLOWUP_FRACTAL_RESPONSE : ''
		},

		FRACTAL_RESPONSE : {
			RESPONSE_TEXT : '',
			FOLLOWUP_DESCRIPTION : '',
			FOLLOWUP_LITERAL_RESPONSE : '',
			FOLLOWUP_FRACTAL_RESPONSE : ''
		}
	}

	'How' : {
		DESCRIPTION : '',
		LITERAL_RESPONSE : {
			RESPONSE_TEXT : '',
			FOLLOWUP_DESCRIPTION : '',
			FOLLOWUP_LITERAL_RESPONSE : '',
			FOLLOWUP_FRACTAL_RESPONSE : ''
		},

		FRACTAL_RESPONSE : {
			RESPONSE_TEXT : '',
			FOLLOWUP_DESCRIPTION : '',
			FOLLOWUP_LITERAL_RESPONSE : '',
			FOLLOWUP_FRACTAL_RESPONSE : ''
		}
	}
}

Dream_Space = {
	'Dragon Slayer' : {
		EXPOSITION : {
			DESCRIPTION : '',
			AGRESSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
			PASSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
		}
		SETUP : {
			DESCRIPTION : '',
			AGRESSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
			PASSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
		}
		ACTION : {
			DESCRIPTION : '',
			AGRESSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
			PASSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
		}
		CLIMAX : {
			DESCRIPTION : '',
			AGRESSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
			PASSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
			SMART_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
		}
	}

	'Alien Survival' : {
		EXPOSITION : {
			DESCRIPTION : '',
			AGRESSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
			PASSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
		}
		SETUP : {
			DESCRIPTION : '',
			AGRESSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
			PASSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
		}
		ACTION : {
			DESCRIPTION : '',
			AGRESSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
			PASSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
		}
		CLIMAX : {
			DESCRIPTION : '',
			AGRESSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
			PASSIVE_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
			SMART_CHOICE : {
				CHOICE_TEXT : '',
				FOLLOWUP_DESCRIPTION : ''
			}
		}
	}
}