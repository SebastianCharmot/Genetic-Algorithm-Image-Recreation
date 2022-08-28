<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Genetic Algorithm for Image Recreation</h3>

  <p align="center">
    A from scratch Python implementation of a genetic algorithm that recreates a target image. 
    <br />
    <!-- <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a> -->
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction-to-genetic-algorithms">Introduction to Genetic Algorithms</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<p>

<!-- ABOUT THE PROJECT -->
## Introduction to Genetic Algorithms

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

In this section, I give a general overview of what a genetic algorithm is. Readers that are familiar with this concept can skip to the next section. 

A genetic algorithm is an optimization tool inspired by Darwin's theory of evolution. The algorithm mimics the process of natural selection, which chooses the fittest individuals from a population to create offspring and populate future generations. 

A genetic algorithm consists of the main components below. Click on any of the triangles to read a definition of each. 

<ul style="list-style: none;">
 <li>
    <details>
        <summary>Initial Population</summary>
        The genetic algorithm starts with a group of individuals, referred to as the initial population. Each individual is a solution for the target that we are optimizing for. Typically, the individuals of the initial population are created randomly, assuming no prior knowledge about the solution. Because the individuals of the initial population are created randomly, they are likely poor solutions. However, their sole purpose is to serve as the building blocks for future generations.
    </details>
  </li>
  <li>
    <details>
        <summary>Fitness Function</summary>
        Once an initial population is created, the individuals are evaluated based on a fitness function. The fitness function is  a metric that evaluates what our genetic algorithm is seeking to optimize. In the classic genetic algorithm example of binary strings with a target, this fitness function might be how many binary strings have the correct value. In this case, a higher fitness function is a string that is "more fit" and closer to the optimal value.
    </details>
  </li>
   <li>
    <details>
        <summary>Selection Criteria</summary>
        The selection criteria determines which individuals from the population are chosen to be parents for the next generation. Typically, we want to select individuals with stronger fitness. However, if we only select individuals with very strong fitness, we will lose some biodiversity. In terms of our algorithm, we want to maintain a certain level of stochasticity within each population to avoid falling into local minima. The classic way parent selection is done is via tournament selection. In essence, X individuals are selected from the total population and the most fit individual from those X tournament participants is chosen to be the parent. We can see that the lower X is, the more stochasticity and biodiversity we introduce into our parent selection. Finding the optimal balance between selecting generally more fit individuals while also maintaining a diverse set of parents is one of the challenging but fun aspects of genetic algorithms.
    </details>
  </li>
  <li>
    <details>
        <summary>Crossover</summary>
        The crossover methods we implement determine how the offspring are created once we have selected parents. Typically two parents are chosen to create offspring. The purpose of a crossover function is to try to combine the attributes of the two parents into a child that is more fit. In order to do so, a popular method is simply to take the first half of parent(1) and combine it with the second half of parent(2). A random "crossover point" can also be used, meaning that parent(1) is used up until the crossover point and then parent(2) is used after the crossover point. Regardless of how crossover is implemented, the hope is that the child will incorporate elements of both parents and have a higher fitness.
    </details>
  </li>
  <li>
    <details>
        <summary>Mutation</summary>
        Mutations are relatively low probability operations that slightly alter an offspring. The purpose of mutations are to introduce stochasticity, which can help combat local optima.
    </details>
  </li>
</ul>

Putting together these components, we have the foundation for a genetic algorithm. We combine them in the following order. First, an initial population is seeded. It's individuals are evaluated by the fitness function, and then our selection criteria chooses fit parents to crossover and populate the next population. Each time a child is produced, there is a potential it will mutate. 

We can repeat the process of creating future generations for a set number of generations or until an optimal solution is achieved. 

Now that we have introduced a genetic algorithm, we can dive into my genetic algorithm that seeks to recreate an image.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* [![Python][Python]][Python-url]

Using the following libraries:

* [Pillow](https://pillow.readthedocs.io/en/stable/index.html) (Image manipulation)
* [Matplotlib](https://matplotlib.org/) (Image display)
* [Numpy](https://numpy.org/) (Perform vectorized image manipulation and calculations)
* [Colour](https://colour.readthedocs.io/en/latest/index.html) (Delta E calculations)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png

[Python]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org/
