//alert("HI")

// fetch() method in js is used to request the server and load the information in the webpages. The request can be of any APIs that returns the data of the format JSON

//Syntax: fetch('url', options)
	//url- this is the url to which the request is to be made.
	//options- an array of properties. it is an optional parameter.
fetch('https://jsonplaceholder.typicode.com/posts').then((response) => response.json()).then((data) => showPosts(data));

//show post function

const showPosts = (posts) => {

	let = postEntries = '';

	posts.forEach((post) =>{
		postEntries += `

		<div id="post-${post.id}">

			<h3 id="post-title-${post.id}">${post.title}</h3>
			<p id="post-body-${post.id}">${post.body}</p>
			<button onclick="editPost('${post.id}')">Edit</button>
			<button onclick="deletePost('${post.id}')">Delete</button>
		</div>
		`;
	});

	document.querySelector("#div-post-entries").innerHTML = postEntries;
};

// ADD POST

document.querySelector("#form-add-post").addEventListener("submit", (e) => {

	e.preventDefault();

	fetch('https://jsonplaceholder.typicode.com/posts', {

		method: 'POST',
		body: JSON.stringify({

			title: document.querySelector("#txt-title").value,
			body: document.querySelector("#txt-body").value,
			userId: 1
		}),
		headers: {'Content-Type': 'application/json'}
	})
	.then((response) => response.json())
	.then((data) => {
		console.log(data)
		alert('Post succesfully added!')
		
		document.querySelector('#txt-title').value = null;
		document.querySelector('#txt-body').value = null;
	})
})

// EDIT POST

const editPost = (id) => {

	let title = document.querySelector(`#post-title-${id}`).innerHTML;

	let body = document.querySelector(`#post-body-${id}`).innerHTML;

	document.querySelector("#txt-edit-id").value = id;

	document.querySelector("#txt-edit-title").value = title;

	document.querySelector("#txt-edit-body").value = body;

	document.querySelector("#btn-submit-update").removeAttribute('disabled');

};


// Update Post

document.querySelector("#form-edit-post").addEventListener("submit", (e) => {

	e.preventDefault();

	fetch('https://jsonplaceholder.typicode.com/posts/1', {

		method: 'PUT',
		body: JSON.stringify({

			id: document.querySelector("#txt-edit-id").value,
			title: document.querySelector("#txt-edit-title").value,
			body: document.querySelector("#txt-edit-body").value,
			userId: 1
		}),

		headers: {'Content-Type': 'application/json'}
	})
	.then((response) => response.json())
	.then((data) => {
		console.log(data)
		alert('Post succesfully updated!')
		
		document.querySelector('#txt-edit-id').value = null;
		document.querySelector('#txt-edit-title').value = null;
		document.querySelector('#txt-edit-body').value = null;
		document.querySelector("#btn-submit-update").setAttribute('disabled', true);
	})
});


//DELETING
//ACTIVITY 
const deletePost = (id) => {
	fetch('https://jsonplaceholder.typicode.com/posts/1', {
		method: 'DELETE'
	})
	.then((data) => {
		document.querySelector(`#post-${id}`).remove()
		console.log(data)
		alert('Post succesfully deleted!')
	})
};




