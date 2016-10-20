var chartjg = c3.generate({
					size: {
							height: 440,
							width: 580
						},
					bindto: '#chartParC',
					data: {
						url: 'data/jobgrowth2.csv'
					},
					axis: {
						x: {
							type: 'category',
							categories: ['2011','2012','2013','2014'],
							tick: {
								outer : false
							},
							//height:0.5
						},
						y:{
						 show: false,
						 max:20,
						 min: 1
						},
						
					},
					grid: {
						x: {
							lines: [							
								{value: 0},
								{value: 1},
								{value: 2},
								{value: 3}
							]
						}
					}
				});
				
