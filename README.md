# RabbitMQ Monitoring

Simple example that illustrates how to configure CollectD to monitor the
activity of a RabbitMQ node.


### Technology stack

- [Docker](https://www.docker.com/)
- [CollectD](https://collectd.org/)
- [CollectD's RabbitMQ plugin](https://github.com/NYTimes/collectd-rabbitmq)
- [CollectD's Graphite plugin](https://collectd.org/wiki/index.php/Plugin:Write_Graphite)
- [Graphite](https://graphiteapp.org/)


### Usage

```bash
make build up
```

Point your browser to **localhost:8080**.

> You probably want to adjust Graphite to show only the past few minutes
> of data. Otherwise, it may be difficult to see any activity in the
> graphs.

### Author(s)

  - Enrique Fernandez `<efcasado(at)gmail.com>`


### License

> The MIT License (MIT)
>
> Copyright (c) 2016, Enrique Fernandez
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.