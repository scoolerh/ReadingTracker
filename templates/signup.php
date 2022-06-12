<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Reading Tracker</title>
        <link rel="stylesheet" href="../static/stylesheet.css">
    </head>

    <body>
        <header> 
            <h1>Reading Tracker</h1>
        </header>

        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/signup">Sign Up</a></li>
                <li><a href="/login">Log In</a></li>
                <li><a href="/pagetracker">Page Tracker</a></li>
                <li><a href="/completedbooks">My Books</a></li>
                <li><a href="/stats">My Stats</a></li>
            </ul>
        </nav>

        <main>
            <section class="signup-form">
                <h2>Sign Up</h2>
                <form action="signup-inc.php" method="post">
                    <input type="text" name="name" placeholder="Full Name">
                    <input type="text" name="email" placeholder="Email">
                    <input type="text" name="username" placeholder="Username">
                    <input type="password" name="password" placeholder="Password">
                    <input type="password" name="passwordrpt" placeholder="Repeat Password">
                    <button type="submit" name="submit">Sign Up</button>
                </form>
            </section>
        </main>

        <footer>
            <p>&copy;Hannah Scooler, 2022</p>
        </footer>
    </body>
</html>