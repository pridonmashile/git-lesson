// Book catalog data
let books = [
    { id: 1, title: 'Book 1', author: 'Author 1', isbn: '1234567890' },
    { id: 2, title: 'Book 2', author: 'Author 2', isbn: '2345678901' },
    { id: 3, title: 'Book 3', author: 'Author 3', isbn: '3456789012' },
];

// Member data
let members = [
    { id: 1, name: 'Member 1', password: 'password1' },
    { id: 2, name: 'Member 2', password: 'password2' },
    { id: 3, name: 'Member 3', password: 'password3' },
];

// Borrowing data
let borrowings = [];

// Search book catalog
document.getElementById('search-btn').addEventListener('click', () => {
    let searchInput = document.getElementById('search-input').value;
    let searchResults = document.getElementById('search-results');
    searchResults.innerHTML = '';

    books.forEach((book) => {
        if (book.title.includes(searchInput) || book.author.includes(searchInput) || book.isbn.includes(searchInput)) {
            let li = document.createElement('li');
            li.textContent = `${book.title} by ${book.author} (ISBN: ${book.isbn})`;
            searchResults.appendChild(li);
        }
    });
});

// Member login
document.getElementById('login-btn').addEventListener('click', (e) => {
    e.preventDefault();
    let memberId = document.getElementById('member-id').value;
    let password = document.getElementById('password').value;

    let member = members.find((member) => member.id === parseInt(memberId) && member.password === password);

    if (member) {
        alert(`Welcome, ${member.name}!`);
    } else {
        alert('Invalid member ID or password');
    }
});

// Checkout book
document.getElementById('checkout-btn').addEventListener('click', () => {
    let bookId = prompt('Enter book ID:');
    let memberId = prompt('Enter member ID:');

    let book = books.find((book) => book.id === parseInt(bookId));
    let member = members.find((member) => member.id === parseInt(memberId));

    if (book && member) {
        borrowings.push({ bookId: book.id, memberId: member.id, borrowDate: new Date(), dueDate: new Date(Date.now() + 14 * 24 * 60 * 60 * 1000) });
        alert(`Book ${book.title} checked out to ${member.name}`);
    } else {
        alert('Invalid book ID or member ID');
    }
});

// Return book
document.getElementById('return-btn').addEventListener('click', () => {
    let bookId = prompt('Enter book ID:');

    let borrowing = borrowings.find((borrowing) => borrowing.bookId === parseInt(bookId));

    if (borrowing) {
        let returnDate = new Date();
        let lateFees = calculateLateFees(borrowing.dueDate, returnDate);
        alert(`Book returned. Late fees: $${lateFees}`);
        borrowings = borrowings.filter((borrowing) => borrowing.bookId !== parseInt(bookId));
    } else {
        alert('Book not found');
    }
});

// Calculate late fees
function calculateLateFees(dueDate, returnDate) {
    let lateDays = Math.floor((returnDate - dueDate) / (24 * 60 * 60 * 1000));
    return lateDays * 0.5;
}