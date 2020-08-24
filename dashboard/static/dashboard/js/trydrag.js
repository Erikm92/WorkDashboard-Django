
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
const el2 = document.getElementById('items2');

Sortable.create(el2, { 
    group:{
        name:'shared',
      //  pull: 'cloned'
    },
    animation: 150,
    chosenClass: "selected",
    onEnd: () =>{

    },
    group: "table_3",
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
const el3 = document.getElementById('items3');

Sortable.create(el3, { 
    group:{
        name:'shared',
      //  pull: 'cloned'
    },
    animation: 150,
    chosenClass: "selected",
    onEnd: () =>{

    },
    group: "table_4",
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
const el4 = document.getElementById('items4');

Sortable.create(el4, { 
    group:{
        name:'shared',
      //  pull: 'cloned'
    },
    animation: 150,
    chosenClass: "selected",
    onEnd: () =>{

    },
    group: "table_5",
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
const el5 = document.getElementById('items5');

Sortable.create(el5, { 
    group:{
        name:'shared',
      //  pull: 'cloned'
    },
    animation: 150,
    chosenClass: "selected",
    onEnd: () =>{

    },
    group: "table_6",
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
const el6 = document.getElementById('items6');

Sortable.create(el6, { 
    group:{
        name:'shared',
      //  pull: 'cloned'
    },
    animation: 150,
    chosenClass: "selected",
    onEnd: () =>{

    },
    group: "table_7",
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
const el7 = document.getElementById('items7');

Sortable.create(el7, { 
    group:{
        name:'shared',
      //  pull: 'cloned'
    },
    animation: 150,
    chosenClass: "selected",
    onEnd: () =>{

    },
    group: "table_8",
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

const el8 = document.getElementById('items8');

Sortable.create(el8, { 
    group:{
        name:'shared',
      //  pull: 'cloned'
    },
    animation: 150,
    chosenClass: "selected",
    onEnd: () =>{

    },
    group: "table_9",
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
const el9 = document.getElementById('items9');

Sortable.create(el9, { 
    group:{
        name:'shared',
      //  pull: 'cloned'
    },
    animation: 150,
    chosenClass: "selected",
    onEnd: () =>{

    },
    group: "table_10",
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
const el10 = document.getElementById('items10');

Sortable.create(el10, { 
    group:{
        name:'shared',
      //  pull: 'cloned'
    },
    animation: 150,
    chosenClass: "selected",
    onEnd: () =>{

    },
    group: "table_11",
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
const el11 = document.getElementById('items11');

Sortable.create(el11, { 
    group:{
        name:'shared',
      //  pull: 'cloned'
    },
    animation: 150,
    chosenClass: "selected",
    onEnd: () =>{

    },
    group: "table_12",
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