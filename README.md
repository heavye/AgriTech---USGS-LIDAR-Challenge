<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
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
<p align="center">
  <a href="https://github.com/heavye/AgriTech---USGS-LIDAR-Challenge">
    <img src="https://user-images.githubusercontent.com/49339609/130367706-8edd52f0-33b1-46de-a656-ed567fdafba4.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">AgriTech USGS LIDAR</h3>

  <p align="center">
    A python module for data fetching and preprocessing from a lidar point cloud in a public dataset on Amazon.
    <br />
    <a href="https://sites.google.com/view/agritech---usgs-lidar/home"><strong>Explore the documentation»</strong></a>
    <br />
    <br />
    <a href="https://registry.opendata.aws/usgs-lidar/">Public dataset on Amazon</a>
    ·
    <a href="https://github.com/heavye/AgriTech---USGS-LIDAR-Challenge/issues">Report Bug</a>
    ·
    <a href="https://github.com/heavye/AgriTech---USGS-LIDAR-Challenge/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
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
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![unnamed](https://user-images.githubusercontent.com/49339609/130367914-2973f6ae-6243-4de7-9ac1-b2be1becba0f.jpg)

LIDAR systems allow scientists and mapping professionals to examine both natural and manmade environments with accuracy, precision, and flexibility. NOAA scientists are using LIDAR to produce more accurate shoreline maps, make digital elevation models for use in geographic information systems, to assist in emergency response operations, and in many other applications."

Agriculture, for example, Water is very important for crop growth and health.  We can better predict maize harvest if we better understand how water flows through a field, and which parts are likely to be flooded or too dry. One important ingredient to understanding water flow in a field is by measuring the elevation of the field at many points. The [USGS recently released high resolution elevation data](https://www.google.com/url?q=https%3A%2F%2Fwww.usgs.gov%2Fnews%2Fusgs-3dep-lidar-point-cloud-now-available-amazon-public-dataset&sa=D&sntz=1&usg=AFQjCNFifksN565iSM_cRehQVpffgMxvQA) as a lidar point cloud called [USGS 3DEP](https://www.google.com/url?q=https%3A%2F%2Fwww.usgs.gov%2Fcore-science-systems%2Fngp%2F3dep&sa=D&sntz=1&usg=AFQjCNGk4PKyPTyW8-1SfC0QV0IbseWoqQ) in a [public dataset on Amazon.](https://www.google.com/url?q=https%3A%2F%2Fregistry.opendata.aws%2Fusgs-lidar%2F&sa=D&sntz=1&usg=AFQjCNGBeJrvSRBkeQjRSyAazn4wvcoXQw) This dataset is essential to build models of water flow and predict plant health and maize harvest. 

Here's What this module can do:
* Fetch the data using PDAL pipeline
* Preprocess in the way through the pipeline
* .LAZ and .LAS files are served right away in the data folder for you to play with it :smile:

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With

Resoures that used in this project are :
* [PDAL](https://pdal.io/)
* [Compression](https://laszip.org)
* [Organization](https://entwine.io)
* [Translation](https://pdal.io)
* [Exploitation](http://lastools.org, https://pdal.io, https://grass.osgeo.org)
* [Visualization](http://potree.org/)
* [CloudCompare](http://plas.io)




<!-- GETTING STARTED -->
## Getting Started

You can get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/heavye/AgriTech---USGS-LIDAR-Challenge.git
   ```
   =======================
   TO BE CONTINUED ...
   ======================
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```JS
   const API_KEY = 'ENTER YOUR API';
   ```



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





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
