var ppp;
$(document).ready(function() {
	$('#myCarousel').carousel();
			// The default axis is 'y', but in this demo, I want to scroll both
			// You can modify any default like this

	$('.navbar-wrapper').localScroll({
           target:'body',
           offset: { top: -60, left: 0 }
    });


	$('.btn-primary').click(function(e) {
		e.preventDefault();
		$("#joyRideTipContent").joyride({
			'tipLocation': 'top'
		});
	});


	var employment_paper = Raphael("employment", $('#employment').width(), 400);

	var unemp_rates = [6.7, 3.5, 9.7, 7.5, 6, 9.6, 9.6, 8.9, 8.1];
	var unemp_years = [1961, 1969, 1982, 1992, 2003, 2009, 2010, 2012];

	for (i = 0; i < unemp_years.length; i++) {
		employment_paper.text(20, 40 + 50 * i, unemp_years[i]).attr({font: "16px sans-serif"});
		var j = 0;
		for (; j < ~~unemp_rates[i]; j++) {
			var p = employment_paper.image('/static/img/small-man.gif', 50 + j * 30, 10 + 50 * i, 23, 44);
			p.hover(function() {
				this.stop();
		    	this.scale(1.3, 1.3, this.cx, this.cy);
			}, function() {
				this.animate({ transform: 's1 1 ' + this.cx + ' ' + this.cy }, 500, "bounce");
			})
		}
		var scale = (unemp_rates[i] - ~~unemp_rates[i]);
		var p = employment_paper.image('/static/img/small-man.gif', 50 + j * 30, 10 + 50 * i + (1-scale)*44, scale * 23, scale * 44);
		p.hover(function() {
				this.stop();
		    	this.scale(1.3, 1.3, this.cx, this.cy);
			}, function() {
				this.animate({ transform: 's1 1 ' + this.cx + ' ' + this.cy }, 500, "bounce");
			})
	}



	var bailout_paper = Raphael("bailout", $('#bailout').width(), 400);
	var amnts = [37, 25, 1];
	var x = 10, y = 250, w = 47, h = 25;
	for (var i = 0; i < amnts.length; i++) {
		var amount = amnts[i];
		var yy = y, xx = x;
		for (var j = 0; j < amount; j++) {
			bailout_paper.image('/static/img/cash.jpg', xx + (w * ~~(j / 10)), yy - (h * ~~(j % 10)), w, h);
		}
		x += Math.ceil(amount/10) * w + 150;
		y = 250;
	}
	bailout_paper.text(100, 300, "Bailout during Financial Crisis: $710bn").attr({font:"10px sans-serif"});
	bailout_paper.text(460, 300, "NASA's funding since founded in 1958: $526bn").attr({font:"10px sans-serif"});
	bailout_paper.text(700, 300, "NASA's funding in 2012: $18bn").attr({font:"10px sans-serif"});





	var budget_pie = Raphael("budget", $('#budget').width(), 500) 
	var pie = budget_pie.piechart(230, 230, 200, [779, 712, 579, 845, 139, 79, 42, 23, 17, 224, 129, 102, 62, 56, 32, 31, 19, 13], {
		legend: ["%%.% - Social Security",
		"%%.% - Defence",
		"%%.% - Income Security",
		"%%.% - Health & Medicare",
		"Education",
		"Housing Credit",
		"Environment",
		"Energy",
		"%%.% - NASA",
		"Net Interest",
		"Veteran Services",
		"Transport",
		"Justice",
		"International affairs",
		"General Government",
		"Community Development",
		"Agriculture",
		"Other Sciences"]
	});
	var nasalogo = budget_pie.image('/static/img/nasalogo.jpg', 700, 50, 0, 0);
	var budget_t = budget_pie.text(500, 360, "Try to find NASA").attr({font: "16px sans-serif"});
	var found = false;
	pie.hover(function () {
	    this.sector.stop();
	    this.sector.scale(1.1, 1.1, this.cx, this.cy);

    	ppp=this;

	    if (this.label) {
	        this.label[0].stop();
	        this.label[0].attr({ r: 7.5 });
	        this.label[1].attr({ "font-weight": 800 });
	    }
	    if (this.label[1].attrs.text.indexOf("Others") !== -1 && found == false) {
	    	found = true;
	    	// found nasa

			var found_t = budget_pie.text(800, 360, "NASA only receives 0.5% of the budget").attr({font: "16px sans-serif"});
			budget_t.hide();
	    	nasalogo.animate({width: 340, height: 293}, 2000, ">", function() {
		    	nasalogo.animate({width: 30, height: 25, x:100, y:100}, 2000, ">")
	    	});

	    	// animate logo bigger
	    	// move it into pie chart

	    }
	}, function () {
	    this.sector.animate({ transform: 's1 1 ' + this.cx + ' ' + this.cy }, 500, "bounce");

	    if (this.label) {
	        this.label[0].animate({ r: 5 }, 500, "bounce");
	        this.label[1].attr({ "font-weight": 400 });
	    }
	});

	$('#responsibility a').lightBox(); // Select all links in object with gallery ID
	
});
