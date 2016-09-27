
var TodoList=Backbone.Model.extend({
    default:{
        name:'',
        created:''
    }
});

var TodoListItems=Backbone.Collection.extend({
    model:TodoList,
     url:'http://127.0.0.1:8000/todolist/',
    
});

//var todo=new TodoList({name:'cprogramming',id:1,created:'25-05-2016'});
var todos=new TodoListItems();



var TodoItemView = Backbone.View.extend({
    template:_.template($('#listscript').html()),
    initialize:function(){
      this.render(); 
    },
    events:{
      'click #item':'showclick',
        'click #deleteitem':'deletemodel',
        'click #edititem':'editmodel',
    },
    showclick:function(){
      console.log(this.model.get('name'));  
    },
    deletemodel:function(){
      this.model.destroy();
        this.remove();
    },
    editmodel:function(){
      var name=prompt("enter new title");
        this.model.save({name:name});
        console.log(name);
        this.render();
    },
    render:function(){
      this.$el.html(this.template(this.model.toJSON()));  
        return this;
    },
});

var TodoListView=Backbone.View.extend({
    el:'#listview',
    initialize:function(){
        var self=this;
         this.collection.fetch({
            success: function(collection, response, options) {
                self.render();
            },
            error: function(model, responce, options) {
                console.log(options.xhr);
            }
        });
    },
    render:function(){
    this.collection.each(function(todoitem){
       var v=new TodoItemView({model:todoitem});
        this.$el.append(v.el);
    },this);
        return this;
}
});


var AppView=Backbone.View.extend({
    el:$('#itemlist'),
   initialize:function(){
     this.render();  
   },events:{
     'keypress #inputitem':'keyPressFunction'
   },
    keyPressFunction:function(e){
      if(e.keyCode==13)
          {
              var string=$('#inputitem').val();
              console.log(string);
              $('#inputitem').val('')
              var t=new TodoList({name:string,created:'2016-05-23'});
              todos.create(t);
              this.addOne(t);
          }
    },
    render:function(){
        todos.fetch();
        var v=new TodoListView({collection:todos});
        console.log(todos);
    },
     addOne:function(todo){
      var v=new TodoItemView({model:todo});
        this.$('#listview').append(v.el);
    },
});

$('document').ready(function(){
    console.log("File successfully compiled");
    //var v=new TodoItemView({model:todo,el:$('#item1')});
    //var v2=new TodoItemView({model:todo1,el:$('#item1')})
    //var v=new TodoListView({collection:todos});
    var a=new AppView();
});



function createCORSRequest(method, url){
    var xhr = new XMLHttpRequest();
    if ("withCredentials" in xhr){
        xhr.open(method, url, true);
    } else if (typeof XDomainRequest != "undefined"){
        xhr = new XDomainRequest();
        xhr.open(method, url);
    } else {
        xhr = null;
    }
    return xhr;
}
/*
var request = createCORSRequest("get", "http://www.nczonline.net/");
if (request){
    request.onload = function(){
        //do something with request.responseText
    };
    request.send();
}*/