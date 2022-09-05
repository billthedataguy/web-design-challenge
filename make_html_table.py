import pandas as pd

csvpath = "Resources/cities.csv"
table = pd.read_csv(csvpath, encoding="utf-8", sep=",")

# print(table)

html = table.to_html(index=False, classes="table")

datahtml_above_table = '''

<!DOCTYPE html>
<html lang="en-us">

<head>
  <meta charset="UTF-8">
  <title>Data</title>

  <!-- Set the viewport the way Bootstrap likes it -->
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- Bring in the Bootstrap stylesheet -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">

  <!-- Bring in our own stylesheet, AFTER Bootstrap  -->
  <link rel="stylesheet" href="/assets/css/style.css">
</head>

<body>
  <nav class="navbar navbar-expand-sm navbar-light bg-light">

	  <div class="container-fluid ">

		  <a class="navbar-brand " href="/index.html">Latitude</a>
		  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
		    <span class="navbar-toggler-icon"></span>
		  </button>

		  <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">

		    <ul class="navbar-nav ">
          <li class="nav-item">
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Plots
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="/visualizations/viz1.html">Vizualization 1: (Lat v. Temp)</a></li>
                <li><a class="dropdown-item" href="/visualizations/viz2.html">Vizualization 2: (Lat v. Humi)</a></li>
                <li><a class="dropdown-item" href="/visualizations/viz3.html">Vizualization 3: (Lat v. Clou)</a></li>
                <li><a class="dropdown-item" href="/visualizations/viz4.html">Vizualization 4: (Lat v. Wind)</a></li>
              </ul>
            </li>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="comparisons.html">Comparison</a>
          </li>		
          <li class="nav-item">
            <a class="nav-link" href="data.html">Data</a>
          </li>      
		    </ul>		 

		  </div>

	  </div>
	</nav>

    <div class="table-responsive">



'''

datahtml_below_table = '''

    </div>

    <!-- Import the Bootstrap JavaScript code -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>

</body>

</html>

'''

with open("data.html", "w", encoding="utf-8") as f:
    f.write(datahtml_above_table)
    f.write(html)
    f.write(datahtml_below_table)


