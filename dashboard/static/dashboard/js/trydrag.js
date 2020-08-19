
const el = document.getElementById('items');

Sortable.create(el, {
    group:{
        name:'shared',
     //   pull: 'cloned'
    },
    animation: 150,
    chosenClass: "selected",
    
    onEnd: () =>{

    },
    group: "table_1",
    store:{
        set: (sortable)=>{
            const order = sortable.toArray();
            localStorage.setItem(sortable.options.group.name, order.join('|'));


        },
        get: (sortable) =>{
            const order = localStorage.getItem(sortable.options.group.name);
            return order ? order.split('|') : [] ;
        } 
    }
});

const el1 = document.getElementById('items1');

Sortable.create(el1, { 
    group:{
        name:'shared',
      //  pull: 'cloned'
    },
    animation: 150,
    chosenClass: "selected",
    onEnd: () =>{

    },
    group: "table_2",
    store:{
        set: (sortable)=>{
            const order = sortable.toArray();
            localStorage.setItem(sortable.options.group.name, order.join('|'));


        },
        get: (sortable) =>{
            const order = localStorage.getItem(sortable.options.group.name);
            return order ? order.split('|') : [] ;
        } 
    }

});
