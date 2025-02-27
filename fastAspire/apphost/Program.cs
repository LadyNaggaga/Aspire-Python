using Microsoft.Extensions.Hosting;

var builder = DistributedApplication.CreateBuilder(args);

#pragma warning disable ASPIREHOSTINGPYTHON001
var backend = builder.AddPythonApp("backend", "../backend", "main.py")
    .WithHttpEndpoint(env: "PORT")
    .WithOtlpExporter();
#pragma warning restore ASPIREHOSTINGPYTHON001

var frontend = builder.AddNpmApp("frontend", "../frontend", "dev")
    .WithHttpEndpoint(env: "VITE_PORT")
    .WithEnvironment("BROWSER", "none")
    .WithExternalHttpEndpoints()
    .WithReference(backend);

builder.Build().Run();
