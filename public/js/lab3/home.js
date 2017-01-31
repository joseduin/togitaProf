function HomeVM() {
	var self = this;

	self.new_post= ko.observable('A Personal Post');
	self.posts = ko.observableArray();
	
	self.current_page = 1
	
	self.current_user = 'rvalera'

	load = function() {
		loadTimeline();
	}
	
	loadTimeline = function() {

		$.ajax({
			url : 'entities/timeline',
			dataType : "json",
			data : {
				page : self.current_page
			},
			beforeSend : function() {
			},
			success : function(data) {
				index = 0;
				data.results.forEach(function (element) {
					element.created_relative  = moment(element.created).fromNow();					
					element.comments_count = element.comments.length
					element.can_delete = element.owner.username.valueOf() == self.current_user.valueOf()
					
					ko_element = ko.mapping.fromJS(element);
					self.posts.push(ko_element);
				});	
			}
		});

	}
	
	removePost = function(data) {
		
		alertify.confirm('Confirm Dialog',"Do you want delete this item?",
			function(){
				$.ajax({
					type:"DELETE",
					url : "entities/timeline/"+data.id()+"/",
					dataType : "json",
				 	success : function(data) {
						alertify.success('Data deleted sucesfully!');
				 		self.posts([]);		 		
				 		loadTimeline();		 		
					},
			 	});		
				
			},
			function(){
			});		
		
	}

	saveNewPost = function() {

		$.ajax({
			type:"POST",
			url : "entities/timeline/",
			dataType : "json",
			data : JSON.stringify({"content" : self.new_post(), "owner" : {"username" : self.current_user} }),
		 	success : function(data) {
		 		self.posts([]);		 		
		 		loadTimeline();		 		
			},
	 	});		
		
	}

	
}

homeVM = HomeVM()
ko.applyBindings(homeVM);